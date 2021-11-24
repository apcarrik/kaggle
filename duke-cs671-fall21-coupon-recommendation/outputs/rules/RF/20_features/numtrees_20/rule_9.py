def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon_validity", "instances": 51, "metric_value": 0.8974, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Restaurantlessthan20", "instances": 28, "metric_value": 0.5917, "depth": 2}
		if obj[16]<=2.0:
			# {"feature": "Passanger", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[4]>1:
					# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]>55:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]>2:
								return 'False'
							elif obj[8]<=2:
								return 'True'
							else: return 'True'
						elif obj[3]<=55:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[16]>2.0:
			return 'True'
		else: return 'True'
	elif obj[6]>0:
		# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9986, "depth": 2}
		if obj[9]<=1:
			# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[17]>0.0:
				# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[11]>1:
					# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[19]>1:
								return 'False'
							elif obj[19]<=1:
								return 'True'
							else: return 'True'
						elif obj[0]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[11]<=1:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[12]<=5:
						# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					elif obj[12]>5:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[17]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[9]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
