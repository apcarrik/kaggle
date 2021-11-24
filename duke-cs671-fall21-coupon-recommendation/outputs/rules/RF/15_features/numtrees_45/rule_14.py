def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[3]<=0:
			return 'True'
		elif obj[3]>0:
			# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[4]<=0:
				return 'False'
			elif obj[4]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[7]>0:
			return 'False'
		elif obj[7]<=0:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
