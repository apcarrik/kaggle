def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[1]>0:
		# {"feature": "Education", "instances": 41, "metric_value": 0.9892, "depth": 2}
		if obj[3]>1:
			# {"feature": "Bar", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 4}
				if obj[4]<=7:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>3.0:
								return 'False'
							elif obj[6]<=3.0:
								return 'True'
							else: return 'True'
						elif obj[2]>3:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]>7:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[2]>2:
						return 'True'
					elif obj[2]<=2:
						# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]<=1.0:
								return 'True'
							elif obj[7]>1.0:
								return 'False'
							else: return 'False'
						elif obj[6]>2.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.8113, "depth": 3}
			if obj[4]<=10:
				# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.5226, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[0]>0:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]>-1.0:
									return 'False'
								elif obj[7]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[5]>0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[6]>1.0:
					return 'True'
				else: return 'True'
			elif obj[4]>10:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'
