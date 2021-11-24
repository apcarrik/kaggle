def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[10]<=5:
		# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.9896, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.9457, "depth": 3}
			if obj[12]<=3.0:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[9]>5:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[3]>3:
						return 'False'
					elif obj[3]<=3:
						# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]<=0:
							return 'True'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]<=5:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[3]>0:
						return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]>3.0:
				return 'False'
			else: return 'False'
		elif obj[13]>2.0:
			return 'True'
		else: return 'True'
	elif obj[10]>5:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[9]>0:
			return 'True'
		elif obj[9]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
