def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[8]<=11:
			# {"feature": "Gender", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[4]>0:
				# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[11]<=3.0:
					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[13]<=0:
						return 'True'
					elif obj[13]>0:
						# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>3.0:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		elif obj[8]>11:
			return 'False'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
