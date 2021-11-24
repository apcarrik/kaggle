def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[8]<=3:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[9]<=7:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[11]<=1.0:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[11]>1.0:
				return 'False'
			else: return 'False'
		elif obj[9]>7:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[3]>2:
				# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[14]<=0:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[12]<=2.0:
						return 'False'
					elif obj[12]>2.0:
						return 'True'
					else: return 'True'
				elif obj[14]>0:
					return 'True'
				else: return 'True'
			elif obj[3]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[8]>3:
		return 'True'
	else: return 'True'
