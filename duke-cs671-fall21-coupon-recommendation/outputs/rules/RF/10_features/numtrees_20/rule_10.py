def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[4]<=10:
		# {"feature": "Coupon", "instances": 38, "metric_value": 1.0, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.9427, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[7]>0.0:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[9]>1:
						# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[3]<=1:
							return 'True'
						elif obj[3]>1:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>0:
										return 'True'
									elif obj[8]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]>1:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[9]<=1:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0.0:
							return 'False'
						elif obj[5]>0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[6]>2.0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>1:
						return 'False'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>10:
		# {"feature": "Time", "instances": 13, "metric_value": 0.3912, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
