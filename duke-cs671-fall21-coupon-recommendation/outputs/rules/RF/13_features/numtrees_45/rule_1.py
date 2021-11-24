def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[8]<=0.0:
		return 'True'
	elif obj[8]>0.0:
		# {"feature": "Age", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[4]>0:
			# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
