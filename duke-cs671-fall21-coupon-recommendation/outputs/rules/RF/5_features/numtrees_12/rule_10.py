def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[2]<=8.141176470588235:
		# {"feature": "Education", "instances": 53, "metric_value": 0.9791, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.9896, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Distance", "instances": 48, "metric_value": 0.9799, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Coupon", "instances": 40, "metric_value": 0.9544, "depth": 5}
					if obj[0]<=3:
						return 'True'
					elif obj[0]>3:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]>2.0:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[2]>8.141176470588235:
		# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.8571, "depth": 2}
		if obj[3]>0.0:
			# {"feature": "Education", "instances": 26, "metric_value": 0.7793, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.6292, "depth": 4}
				if obj[0]>2:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[0]<=2:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=0.0:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
