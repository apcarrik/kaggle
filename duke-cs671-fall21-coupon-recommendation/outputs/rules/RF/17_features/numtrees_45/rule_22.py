def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[12]<=2.0:
		# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[3]>2:
				return 'True'
			elif obj[3]<=2:
				# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[11]<=4:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]>1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[11]>4:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[13]<=0.0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[3]>2:
				return 'False'
			elif obj[3]<=2:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[12]>2.0:
		return 'False'
	else: return 'False'
