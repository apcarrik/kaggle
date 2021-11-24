def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 22, "metric_value": 0.684, "depth": 2}
		if obj[1]<=1:
			return 'True'
		elif obj[1]>1:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[2]<=10:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>10:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[2]<=5:
				return 'False'
			elif obj[2]>5:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
