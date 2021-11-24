def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]<=14:
		# {"feature": "Education", "instances": 32, "metric_value": 0.9745, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[0]>1:
					# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>2.0:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[0]>0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[3]>0.0:
					return 'True'
				elif obj[3]<=0.0:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]>14:
		return 'False'
	else: return 'False'
