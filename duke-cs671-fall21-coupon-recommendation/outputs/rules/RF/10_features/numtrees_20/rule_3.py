def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 38, "metric_value": 1.0, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Direction_same", "instances": 34, "metric_value": 0.99, "depth": 3}
			if obj[8]<=0:
				# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9183, "depth": 4}
				if obj[7]>1.0:
					# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[4]>4:
						# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[2]>1:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[9]<=2:
									return 'True'
								elif obj[9]>2:
									return 'False'
								else: return 'False'
							elif obj[2]<=1:
								return 'False'
							else: return 'False'
						elif obj[6]>2.0:
							return 'False'
						else: return 'False'
					elif obj[4]<=4:
						return 'True'
					else: return 'True'
				elif obj[7]<=1.0:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]>2:
							return 'False'
						elif obj[1]<=2:
							# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>6:
								return 'False'
							elif obj[4]<=6:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[8]>0:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>6:
								return 'True'
							elif obj[4]<=6:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]>1.0:
						return 'True'
					else: return 'True'
				elif obj[5]>0.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.3912, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4]<=2:
				return 'False'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
