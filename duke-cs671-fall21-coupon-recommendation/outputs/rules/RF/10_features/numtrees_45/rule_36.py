def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[9]<=2:
		# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Bar", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Coupon", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[7]<=3.0:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[4]<=7:
							# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[3]<=1:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>0.0:
										return 'True'
									elif obj[6]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[3]>1:
								return 'True'
							else: return 'True'
						elif obj[4]>7:
							return 'False'
						else: return 'False'
					elif obj[7]>3.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[9]>2:
		return 'False'
	else: return 'False'
