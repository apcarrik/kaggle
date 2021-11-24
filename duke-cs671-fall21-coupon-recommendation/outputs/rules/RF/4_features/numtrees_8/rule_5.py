def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9719, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 87, "metric_value": 0.8799, "depth": 2}
		if obj[2]<=16:
			# {"feature": "Education", "instances": 81, "metric_value": 0.8438, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 53, "metric_value": 0.9052, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 28, "metric_value": 0.6769, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>16:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 40, "metric_value": 0.9544, "depth": 2}
		if obj[2]<=13:
			# {"feature": "Distance", "instances": 35, "metric_value": 0.9852, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Education", "instances": 28, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>13:
			return 'False'
		else: return 'False'
	else: return 'False'
