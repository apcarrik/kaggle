def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 32, "metric_value": 0.9745, "depth": 2}
		if obj[3]<=12:
			# {"feature": "Bar", "instances": 28, "metric_value": 0.9059, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.7554, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Direction_same", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2:
									return 'False'
								elif obj[7]>2:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[6]>0:
						return 'False'
					else: return 'False'
				elif obj[5]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[4]>1.0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>12:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 19, "metric_value": 0.4855, "depth": 2}
		if obj[2]<=2:
			return 'True'
		elif obj[2]>2:
			# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]>0.0:
				return 'False'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
