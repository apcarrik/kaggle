def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[3]>0:
		# {"feature": "Weather", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[9]<=9:
				# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[8]>0:
						# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[11]<=1.0:
							return 'True'
						elif obj[11]>1.0:
							return 'False'
						else: return 'False'
					elif obj[8]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[9]>9:
				return 'False'
			else: return 'False'
		elif obj[1]>0:
			return 'True'
		else: return 'True'
	elif obj[3]<=0:
		# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[11]<=2.0:
			return 'False'
		elif obj[11]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
