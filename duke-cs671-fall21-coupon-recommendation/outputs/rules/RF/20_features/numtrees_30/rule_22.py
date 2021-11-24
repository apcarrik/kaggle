def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[15]>0.0:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9059, "depth": 2}
		if obj[12]>4:
			# {"feature": "Maritalstatus", "instances": 18, "metric_value": 0.65, "depth": 3}
			if obj[9]>0:
				# {"feature": "Bar", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[14]<=2.0:
					return 'True'
				elif obj[14]>2.0:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=2:
					return 'False'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[12]<=4:
			# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[8]<=2:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[8]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[15]<=0.0:
		return 'False'
	else: return 'False'
