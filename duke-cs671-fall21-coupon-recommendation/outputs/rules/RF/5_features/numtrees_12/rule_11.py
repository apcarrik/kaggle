def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[3]<=1.0:
		# {"feature": "Coupon", "instances": 55, "metric_value": 0.9998, "depth": 2}
		if obj[0]>1:
			# {"feature": "Occupation", "instances": 41, "metric_value": 0.9789, "depth": 3}
			if obj[2]>0:
				# {"feature": "Distance", "instances": 39, "metric_value": 0.9881, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 20, "metric_value": 0.9341, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					# {"feature": "Education", "instances": 19, "metric_value": 0.998, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>1.0:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.8813, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 28, "metric_value": 0.9059, "depth": 3}
			if obj[2]<=18:
				# {"feature": "Education", "instances": 27, "metric_value": 0.8767, "depth": 4}
				if obj[1]<=4:
					# {"feature": "Distance", "instances": 25, "metric_value": 0.9044, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>4:
					return 'True'
				else: return 'True'
			elif obj[2]>18:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
