def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9996, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Occupation", "instances": 109, "metric_value": 0.9824, "depth": 2}
		if obj[2]<=7.559633027522936:
			# {"feature": "Restaurant20to50", "instances": 73, "metric_value": 0.9137, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Coupon", "instances": 69, "metric_value": 0.9321, "depth": 4}
				if obj[0]>1:
					# {"feature": "Education", "instances": 56, "metric_value": 0.8856, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[1]<=4:
						return 'False'
					elif obj[1]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]>7.559633027522936:
			# {"feature": "Education", "instances": 36, "metric_value": 0.9641, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.9457, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Coupon", "instances": 26, "metric_value": 0.9829, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]<=0.0:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>2:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.5033, "depth": 2}
		if obj[2]<=21:
			# {"feature": "Education", "instances": 17, "metric_value": 0.3228, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>21:
			return 'True'
		else: return 'True'
	else: return 'False'
