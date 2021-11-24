def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[14]<=3.0:
		# {"feature": "Passanger", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[0]>0:
			# {"feature": "Maritalstatus", "instances": 29, "metric_value": 0.9991, "depth": 3}
			if obj[8]<=2:
				# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.9911, "depth": 4}
				if obj[16]<=1.0:
					# {"feature": "Education", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[10]<=2:
						# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[7]>1:
							return 'False'
						elif obj[7]<=1:
							# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[18]>1:
								return 'True'
							elif obj[18]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[10]>2:
						# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[7]>4:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[17]<=0:
								return 'False'
							elif obj[17]>0:
								return 'True'
							else: return 'True'
						elif obj[7]<=4:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[16]>1.0:
					# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[15]<=3.0:
						# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[11]<=5:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[3]>2:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]<=2:
									return 'True'
								elif obj[4]>2:
									return 'False'
								else: return 'False'
							elif obj[3]<=2:
								return 'True'
							else: return 'True'
						elif obj[11]>5:
							return 'False'
						else: return 'False'
					elif obj[15]>3.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[8]>2:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[14]>3.0:
		return 'False'
	else: return 'False'
