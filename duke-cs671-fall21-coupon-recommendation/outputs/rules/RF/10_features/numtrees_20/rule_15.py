def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.8479, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9784, "depth": 2}
		if obj[4]<=7:
			# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.8997, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[9]<=1:
							# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0.0:
									return 'False'
								elif obj[5]>0.0:
									return 'True'
								else: return 'True'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						elif obj[9]>1:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[8]<=0:
							# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[9]>2:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0.0:
									return 'False'
								elif obj[6]>0.0:
									return 'True'
								else: return 'True'
							elif obj[9]<=2:
								return 'False'
							else: return 'False'
						elif obj[8]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[4]>7:
			# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[2]>3:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[2]<=3:
					return 'True'
				else: return 'True'
			elif obj[7]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Education", "instances": 22, "metric_value": 0.4395, "depth": 2}
		if obj[3]<=3:
			return 'True'
		elif obj[3]>3:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]>2:
				return 'False'
			elif obj[1]<=2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
