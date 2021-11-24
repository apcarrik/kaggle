def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[8]>1:
		# {"feature": "Income", "instances": 27, "metric_value": 0.9751, "depth": 2}
		if obj[9]<=3:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[2]>1:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[11]>-1.0:
					# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[7]>0:
						# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[1]>0:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[14]<=2:
								# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[5]<=4:
									return 'False'
								elif obj[5]>4:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=2:
										return 'True'
									elif obj[0]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[14]>2:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				elif obj[11]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[9]>3:
			# {"feature": "Gender", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[12]<=1.0:
							return 'False'
						elif obj[12]>1.0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[4]>0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[8]<=1:
		return 'True'
	else: return 'True'
