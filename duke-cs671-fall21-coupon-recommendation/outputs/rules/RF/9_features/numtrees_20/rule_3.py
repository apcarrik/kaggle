def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Time", "instances": 41, "metric_value": 0.9961, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 35, "metric_value": 0.9994, "depth": 3}
			if obj[4]<=6:
				# {"feature": "Passanger", "instances": 21, "metric_value": 0.9587, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[2]>0:
						# {"feature": "Education", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[3]>1:
							# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								return 'False'
							else: return 'False'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[4]>6:
				# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Bar", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[5]<=2.0:
						return 'False'
					elif obj[5]>2.0:
						return 'True'
					else: return 'True'
				elif obj[3]>2:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>2:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>0.0:
							return 'False'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[0]<=2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[5]<=2.0:
				return 'True'
			elif obj[5]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]>2:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[2]<=2:
			return 'False'
		elif obj[2]>2:
			# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=0.0:
				return 'False'
			elif obj[5]>0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
