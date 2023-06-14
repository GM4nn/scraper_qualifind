URL = "https://super.walmart.com.mx/orchestra/graphql/header"
DPTO_TAG = "Departments"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
)
CONTENT_TYPE = "application/json"
DEFAULT_HEADERS = {
    "User-Agent": USER_AGENT,
    "Referer": URL,
    "Content-Type": CONTENT_TYPE,
}
PAYLOAD = {
    "query": 'query Header( $globalHeaderTempoParams:JSON $tenant:String! $pageType:String! ){contentLayout( channel:"WWW" pageType:$pageType tenant:$tenant version:"v1" ){modules(p13n:{}tempo:$globalHeaderTempoParams){name type moduleId matchedTrigger{zone}configs{...on EnricherModuleConfigsV1{zoneV1}...GlobalAlertBar...GlobalHeaderHamburgerNav...GlobalHeaderMenu}}}}fragment GlobalHeaderHamburgerNav on TempoWM_GLASSWWWGlobalHamburgerNavConfigs{subCategory{subLinks{link{linkText title clickThrough{value}uid}icon}}}fragment GlobalHeaderMenu on TempoWM_GLASSWWWGlobalHeaderMenuConfigs{allCategoriesLink{linkText title clickThrough{value}uid}departments{name cta{linkText title clickThrough{value}uid}heading description image{alt assetId assetName clickThrough{value}height src title width size contentType uid}subCategoryGroup{subCategoryHeading subCategoryLinksGroup{subCategoryLink{linkText title clickThrough{value}uid}openInNewTab}}}}fragment GlobalAlertBar on TempoWM_GLASSWWWGlobalAlertBarConfigsV1{athenaEnabled alertBarV1{iconName text link{linkText title clickThrough{value}uid}backgroundColor messageColor showCloseButton}}',
    "variables": {
        "globalHeaderTempoParams": {
            "params": [
                {"key": "zone", "value": "alertBar"},
                {"key": "zone", "value": "hamburgerNav"},
                {"key": "zone", "value": "departmentsMenu"},
                {"key": "zone", "value": "servicesMenu"},
            ]
        },
        "tenant": "MX_GLASS",
        "pageType": "global_header",
    },
}
