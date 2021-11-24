def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 0.9802, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 74, "metric_value": 0.9995, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 67, "metric_value": 0.9986, "depth": 3}
			if obj[2]<=20:
				# {"feature": "Distance", "instances": 66, "metric_value": 0.9993, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>20:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[2]>1:
				return 'False'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 53, "metric_value": 0.8595, "depth": 2}
		if obj[0]>1:
			# {"feature": "Distance", "instances": 38, "metric_value": 0.7425, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 29, "metric_value": 0.4798, "depth": 4}
				if obj[2]<=21:
					return 'True'
				elif obj[2]>21:
					return 'False'
				else: return 'False'
			elif obj[3]>2:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[2]<=11:
					return 'False'
				elif obj[2]>11:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=1:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[2]>5:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=5:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
