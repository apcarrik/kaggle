def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[3]>0:
		# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Bar", "instances": 20, "metric_value": 1.0, "depth": 4}
				if obj[5]>1.0:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[6]>1.0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]>6:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=3:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=6:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[6]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[5]<=1.0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[4]<=6:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[8]>1:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[8]<=1:
								return 'True'
							else: return 'True'
						elif obj[6]>1.0:
							return 'True'
						else: return 'True'
					elif obj[4]>6:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Bar", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[5]>-1.0:
				return 'False'
			elif obj[5]<=-1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=0:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[4]<=12:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[8]<=2:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>2:
				return 'False'
			else: return 'False'
		elif obj[4]>12:
			return 'False'
		else: return 'False'
	else: return 'True'
