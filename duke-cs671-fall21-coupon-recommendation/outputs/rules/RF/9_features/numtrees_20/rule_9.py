def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 2}
		if obj[4]<=10:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Time", "instances": 17, "metric_value": 0.9367, "depth": 4}
				if obj[1]>0:
					# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[3]>0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=1.0:
								return 'False'
							elif obj[6]>1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[8]<=2:
						return 'True'
					elif obj[8]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]>0.0:
						return 'False'
					elif obj[5]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[4]>10:
			# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Bar", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[5]<=0.0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[4]<=7:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[4]>7:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=3:
					return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>0.0:
			return 'True'
		else: return 'True'
	else: return 'True'
