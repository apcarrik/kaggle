def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[5]>0:
		# {"feature": "Weather", "instances": 30, "metric_value": 0.8366, "depth": 2}
		if obj[2]<=0:
			# {"feature": "Income", "instances": 22, "metric_value": 0.9457, "depth": 3}
			if obj[13]>3:
				# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[9]<=2:
					# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[11]<=1:
						return 'True'
					elif obj[11]>1:
						# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[12]>1:
							return 'True'
						elif obj[12]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]>2:
					return 'False'
				else: return 'False'
			elif obj[13]<=3:
				# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[11]<=2:
					# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=4:
								return 'False'
							elif obj[8]>4:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[6]>0:
						return 'False'
					else: return 'False'
				elif obj[11]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>0:
			return 'True'
		else: return 'True'
	elif obj[5]<=0:
		return 'False'
	else: return 'False'
