def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 40, "metric_value": 0.8813, "depth": 2}
		if obj[4]>1:
			# {"feature": "Education", "instances": 35, "metric_value": 0.7755, "depth": 3}
			if obj[3]<=1:
				# {"feature": "Time", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[1]>0:
					# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[7]<=0:
						# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[2]>3:
								# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[8]>1:
									return 'False'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[2]<=3:
								return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							return 'False'
						else: return 'False'
					elif obj[7]>0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0.0:
								return 'False'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]>1:
				return 'False'
			else: return 'False'
		elif obj[4]<=1:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[6]<=1.0:
			return 'True'
		elif obj[6]>1.0:
			# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=0:
						return 'True'
					elif obj[3]>0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
