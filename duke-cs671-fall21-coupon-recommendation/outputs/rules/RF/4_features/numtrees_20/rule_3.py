def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Distance", "instances": 28, "metric_value": 0.9403, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[2]<=13:
				# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]>13:
				# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.7554, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Education", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>10:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
