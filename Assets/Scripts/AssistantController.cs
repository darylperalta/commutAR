using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AssistantController : MonoBehaviour {

	public GameObject assistant;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if (GetComponent<DefaultTrackableEventHandler>().isTracked) {
			assistant.GetComponent<Canvas>().enabled = true;
			//assistant.transform.parent = transform;
			assistant.transform.SetParent(transform, true);
			assistant.transform.localPosition = Vector3.zero;
			assistant.transform.localEulerAngles = new Vector3(90f, 0f, 0f);
		} else {
			if(transform.childCount>0)
				assistant.GetComponent<Canvas>().enabled = false;
		}
	}
}
