def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon_validity", "instances": 20, "metric_value": 0.9928, "depth": 1}
	if obj[6]>0:
		# {"feature": "Passanger", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[1]>0:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[12]<=6:
					# {"feature": "Carryaway", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[16]>1.0:
						return 'False'
					elif obj[16]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[12]>6:
					return 'True'
				else: return 'True'
			elif obj[14]>1.0:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[6]<=0:
		return 'True'
	else: return 'True'
