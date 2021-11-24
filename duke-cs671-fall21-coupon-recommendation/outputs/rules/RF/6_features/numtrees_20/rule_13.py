def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 37, "metric_value": 0.9953, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Occupation", "instances": 27, "metric_value": 0.951, "depth": 3}
			if obj[3]<=9:
				# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[1]>0:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>9:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]>2:
					# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[5]<=1:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						else: return 'False'
					elif obj[5]>1:
						return 'True'
					else: return 'True'
				elif obj[1]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>2:
			# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[5]>1:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[3]>4:
					return 'False'
				elif obj[3]<=4:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[5]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[5]>1:
			return 'True'
		elif obj[5]<=1:
			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=2:
						return 'False'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[4]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
