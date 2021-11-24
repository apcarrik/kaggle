def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[9]<=2:
			# {"feature": "Gender", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[6]>1:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[10]<=4:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=0:
							return 'False'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					elif obj[10]>4:
						return 'True'
					else: return 'True'
				elif obj[6]<=1:
					return 'False'
				else: return 'False'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		elif obj[9]>2:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[14]>1.0:
			return 'True'
		elif obj[14]<=1.0:
			return 'False'
		else: return 'False'
	else: return 'True'
