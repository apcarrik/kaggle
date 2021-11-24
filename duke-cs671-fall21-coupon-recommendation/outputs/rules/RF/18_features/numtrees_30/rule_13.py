def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9403, "depth": 2}
		if obj[10]<=20:
			# {"feature": "Time", "instances": 26, "metric_value": 0.8905, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Weather", "instances": 22, "metric_value": 0.7732, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3712, "depth": 5}
					if obj[16]<=0:
						return 'False'
					elif obj[16]>0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=3:
							return 'True'
						elif obj[3]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>1:
					# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[6]>2:
						return 'False'
					elif obj[6]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>3:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]>1:
					return 'True'
				elif obj[6]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]>20:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
