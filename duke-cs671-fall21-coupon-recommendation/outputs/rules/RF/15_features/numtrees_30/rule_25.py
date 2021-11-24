def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[5]>3:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[8]<=10:
				return 'True'
			elif obj[8]>10:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[7]<=0:
				return 'False'
			elif obj[7]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]<=3:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[11]<=2.0:
			# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[13]<=0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[8]>2:
						return 'True'
					elif obj[8]<=2:
						# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[13]>0:
				return 'False'
			else: return 'False'
		elif obj[11]>2.0:
			return 'False'
		else: return 'False'
	else: return 'False'
