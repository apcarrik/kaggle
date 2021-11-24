def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[11]<=2:
		# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[17]<=2.0:
			# {"feature": "Time", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[4]>0:
				# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[5]>1:
					# {"feature": "Gender", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[7]>0:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[12]<=14:
							# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[15]<=3.0:
								return 'False'
							elif obj[15]>3.0:
								return 'True'
							else: return 'True'
						elif obj[12]>14:
							return 'True'
						else: return 'True'
					elif obj[7]<=0:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[14]<=0.0:
							return 'True'
						elif obj[14]>0.0:
							# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=0:
								return 'False'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=1:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				# {"feature": "Weather", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[14]<=1.0:
							return 'False'
						elif obj[14]>1.0:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[17]>2.0:
			return 'True'
		else: return 'True'
	elif obj[11]>2:
		return 'False'
	else: return 'False'
