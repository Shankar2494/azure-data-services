using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Azure.Identity;
using Azure.Security.KeyVault.Secrets;
using Azure.Core;

namespace dotnet_sample
{
    public class Startup
    {
        // This method gets called by the runtime. Use this method to add services to the container.
        // For more information on how to configure your application, visit https://go.microsoft.com/fwlink/?LinkID=398940
        public void ConfigureServices(IServiceCollection services)
        {
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseRouting();

	    SecretClientOptions options = new SecretClientOptions()
	    {
		    Retry = 
		    {
			    Delay = TimeSpan.FromSeconds(2),
			    MaxDelay = TimeSpan.FromSeconds(20),
			    MaxRetries = 10,
			    Mode = RetryMode.Exponential
		    }
	    };
	    var client = new SecretClient(new Uri("https://kulkv.vault.azure.net/"), new DefaultAzureCredential(),options);
	  KeyVaultSecret secret = client.GetSecret("Tera-github-ka-pwd-kya-hai"); 
	 string secretValue = secret.Value; 

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapGet("/", async context =>
                {
                    await context.Response.WriteAsync(secretValue);
                });
            });
        }
    }
}
