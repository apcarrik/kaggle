def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[12]<=2.0:
		# {"feature": "Passanger", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[0]>0:
			# {"feature": "Income", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[10]>2:
				# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=4:
							return 'True'
						elif obj[6]>4:
							return 'False'
						else: return 'False'
					elif obj[3]>3:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[10]<=2:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[12]>2.0:
		return 'True'
	else: return 'True'
