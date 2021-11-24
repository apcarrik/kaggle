def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9612, "depth": 2}
		if obj[4]>1:
			# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[6]>1.0:
				# {"feature": "Time", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>2:
						return 'False'
					elif obj[2]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]<=1.0:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[8]>1:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[2]>0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>3:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=2:
									return 'False'
								elif obj[3]>2:
									return 'True'
								else: return 'True'
							elif obj[1]<=3:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'False'
					else: return 'False'
				elif obj[8]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=0:
				return 'False'
			elif obj[2]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
