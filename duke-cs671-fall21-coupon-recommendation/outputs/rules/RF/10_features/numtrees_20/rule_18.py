def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]>0:
		# {"feature": "Education", "instances": 37, "metric_value": 0.974, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=3:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								return 'False'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>3:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]>0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[8]>0:
								return 'True'
							elif obj[8]<=0:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[6]<=1.0:
					return 'True'
				elif obj[6]>1.0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[3]>1:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[7]>0.0:
				return 'True'
			elif obj[7]<=0.0:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[4]>2:
			return 'False'
		elif obj[4]<=2:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=1.0:
					return 'True'
				elif obj[7]>1.0:
					return 'False'
				else: return 'False'
			elif obj[3]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
