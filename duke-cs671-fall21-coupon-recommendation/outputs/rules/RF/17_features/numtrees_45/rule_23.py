def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon_validity", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]<=0:
		# {"feature": "Passanger", "instances": 13, "metric_value": 0.9612, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Weather", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	elif obj[4]>0:
		# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[2]<=3:
			return 'False'
		elif obj[2]>3:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
