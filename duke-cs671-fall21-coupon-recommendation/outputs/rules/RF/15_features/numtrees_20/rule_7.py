def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[5]<=4:
		# {"feature": "Coffeehouse", "instances": 42, "metric_value": 0.9403, "depth": 2}
		if obj[11]>0.0:
			# {"feature": "Occupation", "instances": 36, "metric_value": 0.9799, "depth": 3}
			if obj[8]<=16:
				# {"feature": "Time", "instances": 34, "metric_value": 0.9597, "depth": 4}
				if obj[1]>1:
					# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[10]<=2.0:
							# {"feature": "Children", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=0:
										return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[9]<=3:
										return 'False'
									elif obj[9]>3:
										return 'True'
									else: return 'True'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[10]>2.0:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Passanger", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Income", "instances": 15, "metric_value": 0.5665, "depth": 6}
						if obj[9]<=6:
							return 'False'
						elif obj[9]>6:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0:
									return 'True'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]>16:
				return 'True'
			else: return 'True'
		elif obj[11]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[5]>4:
		return 'True'
	else: return 'True'
