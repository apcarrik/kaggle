def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[16]<=0:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[10]>5:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[12]<=0.0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>3:
					# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[17]<=1:
							return 'False'
						elif obj[17]>1:
							return 'True'
						else: return 'True'
					elif obj[4]>0:
						return 'False'
					else: return 'False'
				elif obj[3]<=3:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[10]<=5:
			# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[4]<=0:
				return 'True'
			elif obj[4]>0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[16]>0:
		return 'False'
	else: return 'False'
