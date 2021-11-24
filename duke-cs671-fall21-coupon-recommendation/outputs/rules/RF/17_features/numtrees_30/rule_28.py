def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[3]>0:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9784, "depth": 2}
		if obj[10]>4:
			# {"feature": "Time", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[16]>1:
					# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[13]<=3.0:
						# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[4]<=0:
							return 'True'
						elif obj[4]>0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[13]>3.0:
						return 'False'
					else: return 'False'
				elif obj[16]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]>2:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[14]>0.0:
					return 'False'
				elif obj[14]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]<=4:
			# {"feature": "Income", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[11]>2:
				return 'True'
			elif obj[11]<=2:
				# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]>0:
					return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=0:
		return 'False'
	else: return 'False'
