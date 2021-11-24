def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.999, "depth": 2}
		if obj[3]>0:
			# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[6]<=4:
				# {"feature": "Time", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[2]>0:
					# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[17]>1:
						# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[13]<=2.0:
							return 'False'
						elif obj[13]>2.0:
							# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=0:
								return 'True'
							elif obj[7]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[17]<=1:
						# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[7]<=3:
							return 'True'
						elif obj[7]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[6]>4:
				return 'True'
			else: return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
