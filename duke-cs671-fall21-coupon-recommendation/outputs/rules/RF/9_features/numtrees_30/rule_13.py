def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[5]<=2.0:
		# {"feature": "Distance", "instances": 29, "metric_value": 0.9784, "depth": 2}
		if obj[8]>1:
			# {"feature": "Passanger", "instances": 21, "metric_value": 0.8631, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[4]>1:
								return 'False'
							elif obj[4]<=1:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>2:
									return 'False'
								elif obj[2]<=2:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]>0:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=3:
								return 'True'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[4]>5:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]<=5:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[8]<=1:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]>2.0:
		return 'True'
	else: return 'True'
