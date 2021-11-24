def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[2]>1:
			return 'True'
		elif obj[2]<=1:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[6]>0.0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=15:
					return 'True'
				elif obj[5]>15:
					return 'False'
				else: return 'False'
			elif obj[6]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[5]<=15:
			return 'False'
		elif obj[5]>15:
			return 'True'
		else: return 'True'
	else: return 'False'
