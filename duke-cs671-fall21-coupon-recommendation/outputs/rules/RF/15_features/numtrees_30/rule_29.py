def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[12]<=2.0:
		# {"feature": "Bar", "instances": 30, "metric_value": 1.0, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[13]<=0:
				# {"feature": "Age", "instances": 20, "metric_value": 0.8813, "depth": 4}
				if obj[5]>1:
					# {"feature": "Passanger", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=3:
							return 'False'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=2:
							return 'True'
						elif obj[1]>2:
							# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=1:
					return 'False'
				else: return 'False'
			elif obj[13]>0:
				return 'True'
			else: return 'True'
		elif obj[10]>1.0:
			# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[9]<=6:
				return 'True'
			elif obj[9]>6:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[12]>2.0:
		return 'True'
	else: return 'True'
