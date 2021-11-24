def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[3]>0.0:
		# {"feature": "Distance", "instances": 27, "metric_value": 0.9751, "depth": 2}
		if obj[4]>1:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[2]<=21:
				# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]>21:
				return 'False'
			else: return 'False'
		elif obj[4]<=1:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=6:
					return 'True'
				elif obj[2]>6:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=0.0:
		return 'True'
	else: return 'True'
