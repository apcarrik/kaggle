def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[12]>0.0:
		# {"feature": "Occupation", "instances": 20, "metric_value": 1.0, "depth": 2}
		if obj[8]<=8:
			# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[11]<=1.0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[1]>1:
					# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]>0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=4:
								return 'False'
							elif obj[5]>4:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[11]>1.0:
				return 'True'
			else: return 'True'
		elif obj[8]>8:
			# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[6]<=0:
				return 'False'
			elif obj[6]>0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[12]<=0.0:
		return 'True'
	else: return 'True'
