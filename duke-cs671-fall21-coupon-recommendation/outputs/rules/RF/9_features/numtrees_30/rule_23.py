def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[2]>0:
			# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[4]<=19:
					# {"feature": "Time", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[8]>1:
										return 'False'
									elif obj[8]<=1:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[6]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[4]>19:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[5]>1.0:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[4]<=12:
			# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[3]<=2:
				return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		elif obj[4]>12:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
